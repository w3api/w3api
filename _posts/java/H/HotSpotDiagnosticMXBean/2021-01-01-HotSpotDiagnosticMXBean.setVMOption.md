---
title: HotSpotDiagnosticMXBean.setVMOption()
permalink: /Java/HotSpotDiagnosticMXBean/setVMOption/
date: 2021-01-11
key: Java.H.HotSpotDiagnosticMXBean
category: Java
tags: ['java se', 'com.sun.management', 'jdk.management', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HotSpotDiagnosticMXBean.metodos valor="setVMOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setVMOption(String name, String value)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HotSpotDiagnosticMXBean](/Java/HotSpotDiagnosticMXBean/)

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
