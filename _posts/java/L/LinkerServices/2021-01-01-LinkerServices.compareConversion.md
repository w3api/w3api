---
title: LinkerServices.compareConversion()
permalink: /Java/LinkerServices/compareConversion/
date: 2021-01-11
key: Java.L.LinkerServices
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkerServices.metodos valor="compareConversion" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ConversionComparator.Comparison compareConversion(Class<?> sourceType, Class<?> targetType1, Class<?> targetType2)
~~~

## Parámetros
* **Class&lt;?&gt; targetType1**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> targetType1" %}
* **Class&lt;?&gt; targetType2**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> targetType2" %}
* **Class&lt;?&gt; sourceType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> sourceType" %}

## Clase Padre
[LinkerServices](/Java/LinkerServices/)

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
