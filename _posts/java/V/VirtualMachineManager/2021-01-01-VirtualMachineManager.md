---
title: VirtualMachineManager
permalink: Java/VirtualMachineManager
date: 2021-01-11
key: JavaJava.V.VirtualMachineManager
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.V.VirtualMachineManager.description }}

## Sintaxis
~~~java
public interface VirtualMachineManager
~~~

## Métodos
* [allConnectors()](/Java/VirtualMachineManager/allConnectors)
* [attachingConnectors()](/Java/VirtualMachineManager/attachingConnectors)
* [connectedVirtualMachines()](/Java/VirtualMachineManager/connectedVirtualMachines)
* [createVirtualMachine()](/Java/VirtualMachineManager/createVirtualMachine)
* [defaultConnector()](/Java/VirtualMachineManager/defaultConnector)
* [launchingConnectors()](/Java/VirtualMachineManager/launchingConnectors)
* [listeningConnectors()](/Java/VirtualMachineManager/listeningConnectors)
* [majorInterfaceVersion()](/Java/VirtualMachineManager/majorInterfaceVersion)
* [minorInterfaceVersion()](/Java/VirtualMachineManager/minorInterfaceVersion)

## Ejemplo
~~~java
{{ site.data.Java.V.VirtualMachineManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VirtualMachineManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
