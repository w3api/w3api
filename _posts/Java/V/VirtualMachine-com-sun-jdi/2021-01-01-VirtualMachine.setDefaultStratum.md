---
title: VirtualMachine.setDefaultStratum()
permalink: /Java/VirtualMachine-com-sun-jdi/setDefaultStratum/
date: 2021-01-11
key: Java.V.VirtualMachine-com-sun-jdi
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-jdi.metodos valor="setDefaultStratum" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setDefaultStratum(String stratum)
~~~

## Parámetros
* **String stratum**,  {% include w3api/param_description.html metodo=_dato parametro="String stratum" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[VirtualMachine](/Java/VirtualMachine-com-sun-jdi/)

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
