interface Alert {
  message: string;
  level: "info" | "warning" | "danger";
}

function display(alert: Alert): void {
  console.log(`[${alert.level.toUpperCase()}] ${alert.message}`);
}

display({ message: "Timelytics UI Loaded", level: "info" });