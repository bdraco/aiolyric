"""
Class object for LyricLocation
Documentation: https://github.com/timmo001/aiolyric

Generated by generator/generator.py - 2020-08-31 13:55:49.220121
"""
from Lyric.objects.objects.base import LyricBase


class DevicesVacationhold(LyricBase):

    @property
    def enabled(self):
        return self.attributes.get("enabled", False)


class DevicesCurrentscheduleperiod(LyricBase):

    @property
    def day(self):
        return self.attributes.get("day", "")

    @property
    def period(self):
        return self.attributes.get("period", "")


class DevicesSchedulecapabilities(LyricBase):

    @property
    def availableScheduleTypes(self):
        return self.attributes.get("availableScheduleTypes", [])

    @property
    def schedulableFan(self):
        return self.attributes.get("schedulableFan", False)


class DevicesScheduletype(LyricBase):

    @property
    def scheduleType(self):
        return self.attributes.get("scheduleType", "")

    @property
    def scheduleSubType(self):
        return self.attributes.get("scheduleSubType", "")


class DevicesSettingsHardwaresettings(LyricBase):

    @property
    def brightness(self):
        return self.attributes.get("brightness", None)

    @property
    def maxBrightness(self):
        return self.attributes.get("maxBrightness", None)


class DevicesSettingsTemperaturemode(LyricBase):

    @property
    def air(self):
        return self.attributes.get("air", True)


class DevicesSettingsSpecialmode(LyricBase):


class DevicesSettings(LyricBase):

    @property
    def hardwareSettings(self):
        return DevicesSettingsHardwaresettings(self.attributes.get("hardwareSettings", {}))

    @property
    def temperatureMode(self):
        return DevicesSettingsTemperaturemode(self.attributes.get("temperatureMode", {}))

    @property
    def specialMode(self):
        return DevicesSettingsSpecialmode(self.attributes.get("specialMode", {}))

    @property
    def devicePairingEnabled(self):
        return self.attributes.get("devicePairingEnabled", True)


class DevicesDevicesettings(LyricBase):


class DevicesService(LyricBase):

    @property
    def mode(self):
        return self.attributes.get("mode", "")


class DevicesChangeablevalues(LyricBase):

    @property
    def mode(self):
        return self.attributes.get("mode", "")

    @property
    def heatSetpoint(self):
        return self.attributes.get("heatSetpoint", None)

    @property
    def coolSetpoint(self):
        return self.attributes.get("coolSetpoint", None)

    @property
    def thermostatSetpointStatus(self):
        return self.attributes.get("thermostatSetpointStatus", "")

    @property
    def nextPeriodTime(self):
        return self.attributes.get("nextPeriodTime", "")

    @property
    def heatCoolMode(self):
        return self.attributes.get("heatCoolMode", "")

    @property
    def endHeatSetpoint(self):
        return self.attributes.get("endHeatSetpoint", None)

    @property
    def endCoolSetpoint(self):
        return self.attributes.get("endCoolSetpoint", None)


class DevicesOperationstatus(LyricBase):

    @property
    def mode(self):
        return self.attributes.get("mode", "")

    @property
    def fanRequest(self):
        return self.attributes.get("fanRequest", False)

    @property
    def circulationFanRequest(self):
        return self.attributes.get("circulationFanRequest", False)


class Devices(LyricBase):

    @property
    def displayedOutdoorHumidity(self):
        return self.attributes.get("displayedOutdoorHumidity", None)

    @property
    def vacationHold(self):
        return DevicesVacationhold(self.attributes.get("vacationHold", {}))

    @property
    def currentSchedulePeriod(self):
        return DevicesCurrentscheduleperiod(self.attributes.get("currentSchedulePeriod", {}))

    @property
    def scheduleCapabilities(self):
        return DevicesSchedulecapabilities(self.attributes.get("scheduleCapabilities", {}))

    @property
    def scheduleType(self):
        return DevicesScheduletype(self.attributes.get("scheduleType", {}))

    @property
    def scheduleStatus(self):
        return self.attributes.get("scheduleStatus", "")

    @property
    def allowedTimeIncrements(self):
        return self.attributes.get("allowedTimeIncrements", None)

    @property
    def settings(self):
        return DevicesSettings(self.attributes.get("settings", {}))

    @property
    def deviceClass(self):
        return self.attributes.get("deviceClass", "")

    @property
    def deviceType(self):
        return self.attributes.get("deviceType", "")

    @property
    def deviceID(self):
        return self.attributes.get("deviceID", "")

    @property
    def userDefinedDeviceName(self):
        return self.attributes.get("userDefinedDeviceName", "")

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def isAlive(self):
        return self.attributes.get("isAlive", True)

    @property
    def isUpgrading(self):
        return self.attributes.get("isUpgrading", False)

    @property
    def isProvisioned(self):
        return self.attributes.get("isProvisioned", True)

    @property
    def macID(self):
        return self.attributes.get("macID", "")

    @property
    def deviceSettings(self):
        return DevicesDevicesettings(self.attributes.get("deviceSettings", {}))

    @property
    def service(self):
        return DevicesService(self.attributes.get("service", {}))

    @property
    def deviceRegistrationDate(self):
        return self.attributes.get("deviceRegistrationDate", "")

    @property
    def dataSyncStatus(self):
        return self.attributes.get("dataSyncStatus", "")

    @property
    def units(self):
        return self.attributes.get("units", "")

    @property
    def indoorTemperature(self):
        return self.attributes.get("indoorTemperature", None)

    @property
    def outdoorTemperature(self):
        return self.attributes.get("outdoorTemperature", None)

    @property
    def allowedModes(self):
        return self.attributes.get("allowedModes", [])

    @property
    def deadband(self):
        return self.attributes.get("deadband", None)

    @property
    def hasDualSetpointStatus(self):
        return self.attributes.get("hasDualSetpointStatus", False)

    @property
    def minHeatSetpoint(self):
        return self.attributes.get("minHeatSetpoint", None)

    @property
    def maxHeatSetpoint(self):
        return self.attributes.get("maxHeatSetpoint", None)

    @property
    def minCoolSetpoint(self):
        return self.attributes.get("minCoolSetpoint", None)

    @property
    def maxCoolSetpoint(self):
        return self.attributes.get("maxCoolSetpoint", None)

    @property
    def changeableValues(self):
        return DevicesChangeablevalues(self.attributes.get("changeableValues", {}))

    @property
    def operationStatus(self):
        return DevicesOperationstatus(self.attributes.get("operationStatus", {}))

    @property
    def deviceModel(self):
        return self.attributes.get("deviceModel", "")


class Locationrolemapping(LyricBase):

    @property
    def locationID(self):
        return self.attributes.get("locationID", None)

    @property
    def role(self):
        return self.attributes.get("role", "")

    @property
    def locationName(self):
        return self.attributes.get("locationName", "")

    @property
    def status(self):
        return self.attributes.get("status", None)


class Users(LyricBase):

    @property
    def userID(self):
        return self.attributes.get("userID", None)

    @property
    def username(self):
        return self.attributes.get("username", "")

    @property
    def firstname(self):
        return self.attributes.get("firstname", "")

    @property
    def lastname(self):
        return self.attributes.get("lastname", "")

    @property
    def created(self):
        return self.attributes.get("created", None)

    @property
    def deleted(self):
        return self.attributes.get("deleted", None)

    @property
    def activated(self):
        return self.attributes.get("activated", True)

    @property
    def connectedHomeAccountExists(self):
        return self.attributes.get("connectedHomeAccountExists", True)

    @property
    def locationRoleMapping(self):
        return [Locationrolemapping(x) for x in self.attributes.get("locationRoleMapping", [])]

    @property
    def isOptOut(self):
        return self.attributes.get("isOptOut", "")

    @property
    def isCurrentUser(self):
        return self.attributes.get("isCurrentUser", True)


class Time(LyricBase):

    @property
    def start(self):
        return self.attributes.get("start", "")

    @property
    def end(self):
        return self.attributes.get("end", "")


class Schedules(LyricBase):

    @property
    def time(self):
        return [Time(x) for x in self.attributes.get("time", [])]

    @property
    def days(self):
        return self.attributes.get("days", [])


class ConfigurationFacerecognition(LyricBase):

    @property
    def enabled(self):
        return self.attributes.get("enabled", False)

    @property
    def maxPersons(self):
        return self.attributes.get("maxPersons", None)

    @property
    def maxEtas(self):
        return self.attributes.get("maxEtas", None)

    @property
    def maxEtaPersons(self):
        return self.attributes.get("maxEtaPersons", None)

    @property
    def schedules(self):
        return [Schedules(x) for x in self.attributes.get("schedules", [])]


class Configuration(LyricBase):

    @property
    def faceRecognition(self):
        return ConfigurationFacerecognition(self.attributes.get("faceRecognition", {}))


class LyricLocation(LyricBase):

    @property
    def locationID(self):
        return self.attributes.get("locationID", None)

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def country(self):
        return self.attributes.get("country", "")

    @property
    def zipcode(self):
        return self.attributes.get("zipcode", "")

    @property
    def devices(self):
        return [Devices(x) for x in self.attributes.get("devices", [])]

    @property
    def users(self):
        return [Users(x) for x in self.attributes.get("users", [])]

    @property
    def timeZone(self):
        return self.attributes.get("timeZone", "")

    @property
    def ianaTimeZone(self):
        return self.attributes.get("ianaTimeZone", "")

    @property
    def daylightSavingTimeEnabled(self):
        return self.attributes.get("daylightSavingTimeEnabled", True)

    @property
    def geoFenceEnabled(self):
        return self.attributes.get("geoFenceEnabled", False)

    @property
    def predictiveAIREnabled(self):
        return self.attributes.get("predictiveAIREnabled", False)

    @property
    def comfortLevel(self):
        return self.attributes.get("comfortLevel", None)

    @property
    def geoFenceNotificationEnabled(self):
        return self.attributes.get("geoFenceNotificationEnabled", False)

    @property
    def geoFenceNotificationTypeId(self):
        return self.attributes.get("geoFenceNotificationTypeId", None)

    @property
    def configuration(self):
        return Configuration(self.attributes.get("configuration", {}))


