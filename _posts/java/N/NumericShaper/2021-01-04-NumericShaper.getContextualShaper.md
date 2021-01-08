---
title: NumericShaper.getContextualShaper()
permalink: Java/NumericShaper/getContextualShaper
date: 2021-01-04
key: JavaJava.N.NumericShaper
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumericShaper.metodos valor="getContextualShaper" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static NumericShaper getContextualShaper(int ranges)
public static NumericShaper getContextualShaper(int ranges, int defaultContext)
public static NumericShaper getContextualShaper(Set<NumericShaper.Range> ranges)
public static NumericShaper getContextualShaper(Set<NumericShaper.Range> ranges, NumericShaper.Range defaultContext)
~~~

## Parámetros
* **int defaultContext**,  {% include w3api/param_description.html metodo=_data parametro="int defaultContext" %}
* **NumericShaper.Range defaultContext**,  {% include w3api/param_description.html metodo=_data parametro="NumericShaper.Range defaultContext" %}
* **Set&lt;NumericShaper.Range&gt; ranges**,  {% include w3api/param_description.html metodo=_data parametro="Set<NumericShaper.Range> ranges" %}
* **int ranges**,  {% include w3api/param_description.html metodo=_data parametro="int ranges" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NumericShaper](/Java/NumericShaper/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NumericShaper.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
