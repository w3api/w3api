---
title: AbstractPreferences.putDouble()
permalink: Java/AbstractPreferences/putDouble
date: 2021-01-04
key: JavaJava.A.AbstractPreferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractPreferences.metodos valor="putDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void putDouble(String key, double value)
~~~

## Parámetros
* **double value**,  {% include w3api/param_description.html metodo=_data parametro="double value" %}
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AbstractPreferences](/Java/AbstractPreferences/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractPreferences.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
