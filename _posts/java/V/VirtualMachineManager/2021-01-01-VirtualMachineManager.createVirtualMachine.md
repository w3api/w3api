---
title: VirtualMachineManager.createVirtualMachine()
permalink: /Java/VirtualMachineManager/createVirtualMachine/
date: 2021-01-11
key: Java.V.VirtualMachineManager
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachineManager.metodos valor="createVirtualMachine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
VirtualMachine createVirtualMachine(Connection connection) throws IOException
VirtualMachine createVirtualMachine(Connection connection, Process process) throws IOException
~~~

## Parámetros
* **Connection connection**,  {% include w3api/param_description.html metodo=_dato parametro="Connection connection" %}
* **Process process**,  {% include w3api/param_description.html metodo=_dato parametro="Process process" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[VirtualMachineManager](/Java/VirtualMachineManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
