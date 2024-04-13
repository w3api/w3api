---
title: VirtualMachine.attach()
permalink: /Java/VirtualMachine-com-sun-tools-attach/attach/
date: 2021-01-11
key: Java.V.VirtualMachine-com-sun-tools-attach
category: Java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-tools-attach.metodos valor="attach" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static VirtualMachine attach(VirtualMachineDescriptor vmd) throws AttachNotSupportedException, IOException
public static VirtualMachine attach(String id) throws AttachNotSupportedException, IOException
~~~

## Parámetros
* **VirtualMachineDescriptor vmd**,  {% include w3api/param_description.html metodo=_dato parametro="VirtualMachineDescriptor vmd" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}

## Excepciones
[AttachNotSupportedException](/Java/AttachNotSupportedException/), [SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[VirtualMachine](/Java/VirtualMachine-com-sun-tools-attach/)

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
