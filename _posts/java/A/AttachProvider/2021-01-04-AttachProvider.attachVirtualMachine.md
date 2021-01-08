---
title: AttachProvider.attachVirtualMachine()
permalink: Java/AttachProvider/attachVirtualMachine
date: 2021-01-04
key: JavaJava.A.AttachProvider
category: java
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
* **String id**,  {% include w3api/param_description.html metodo=_data parametro="String id" %}
* **VirtualMachineDescriptor vmd**,  {% include w3api/param_description.html metodo=_data parametro="VirtualMachineDescriptor vmd" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [SecurityException](/Java/SecurityException/), [AttachNotSupportedException](/Java/AttachNotSupportedException/), [IOException](/Java/IOException/)

## Clase Padre
[AttachProvider](/Java/AttachProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttachProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
