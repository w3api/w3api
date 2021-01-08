---
title: HotSpotDiagnosticMXBean.setVMOption()
permalink: Java/HotSpotDiagnosticMXBean/setVMOption
date: 2021-01-04
key: JavaJava.H.HotSpotDiagnosticMXBean
category: java
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
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String value**,  {% include w3api/param_description.html metodo=_data parametro="String value" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HotSpotDiagnosticMXBean](/Java/HotSpotDiagnosticMXBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HotSpotDiagnosticMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
