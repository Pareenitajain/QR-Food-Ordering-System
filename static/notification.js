// ============================================
// NOTIFICATION SYSTEM
// ============================================

let lastOrderId = 0;
let lastOrderCount = 0;

// Play notification sound
function playNotificationSound() {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    // Create a simple beep sound
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.frequency.value = 800; // Frequency in Hz
    oscillator.type = 'sine';
    
    gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
    
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.5);
}

// Show visual notification
function showVisualNotification() {
    const notification = document.getElementById('newOrderNotification');
    if (notification) {
        notification.classList.add('show');
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    }
}

// Check for new orders
function checkForNewOrders() {
    fetch('/api/latest-orders')
        .then(response => response.json())
        .then(orders => {
            if (orders.length > 0) {
                const latestOrder = orders[0];
                
                // Check if there's a new order
                if (latestOrder.id > lastOrderId) {
                    lastOrderId = latestOrder.id;
                    
                    // Play sound and show notification
                    playNotificationSound();
                    showVisualNotification();
                    
                    // Reload page to show new order
                    setTimeout(() => {
                        location.reload();
                    }, 500);
                }
            }
        })
        .catch(error => console.log('Error checking orders:', error));
}

// Update order count
function updateOrderCount() {
    fetch('/api/orders-count')
        .then(response => response.json())
        .then(data => {
            const badge = document.getElementById('orderCountBadge');
            if (badge) {
                badge.innerText = data.count;
            }
        })
        .catch(error => console.log('Error updating count:', error));
}

// Start checking for new orders every 5 seconds
document.addEventListener('DOMContentLoaded', () => {
    updateOrderCount();
    checkForNewOrders();
    
    // Check every 5 seconds
    setInterval(() => {
        checkForNewOrders();
        updateOrderCount();
    }, 5000);
});
