---
title: AbstractPreferences.getFloat()
permalink: Java/AbstractPreferences/getFloat
date: 2021-01-04
key: JavaJava.A.AbstractPreferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractPreferences.metodos valor="getFloat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public float getFloat(String key, float def)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}
* **float def**,  {% include w3api/param_description.html metodo=_data parametro="float def" %}

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
