---
title: LinkerServices.compareConversion()
permalink: Java/LinkerServices/compareConversion
date: 2021-01-04
key: JavaJava.L.LinkerServices
category: java
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
* **Class&lt;?&gt; targetType2**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> targetType2" %}
* **Class&lt;?&gt; sourceType**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> sourceType" %}
* **Class&lt;?&gt; targetType1**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> targetType1" %}

## Clase Padre
[LinkerServices](/Java/LinkerServices/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkerServices.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
