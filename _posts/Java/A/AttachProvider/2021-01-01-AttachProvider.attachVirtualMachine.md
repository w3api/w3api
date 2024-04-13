---
title: AttachProvider.attachVirtualMachine()
permalink: /Java/AttachProvider/attachVirtualMachine/
date: 2021-01-11
key: Java.A.AttachProvider
category: Java
tags: ['java se', 'com.sun.tools.attach.spi', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachProvider.metodos valor="attachVirtualMachine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public VirtualMachine attachVirtualMachine(VirtualMachineDescriptor vmd) throws AttachNotSupportedException, IOException
public abstract VirtualMachine attachVirtualMachine(String id) throws AttachNotSupportedException, IOException
~~~

## Parámetros
* **VirtualMachineDescriptor vmd**,  {% include w3api/param_description.html metodo=_dato parametro="VirtualMachineDescriptor vmd" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}

## Excepciones
[AttachNotSupportedException](/Java/AttachNotSupportedException/), [SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[AttachProvider](/Java/AttachProvider/)

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
