---
title: VirtualMachine.list()
permalink: /Java/VirtualMachine-com-sun-tools-attach/list/
date: 2021-01-11
key: Java.V.VirtualMachine-com-sun-tools-attach
category: Java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-tools-attach.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static List<VirtualMachineDescriptor> list()
~~~

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
