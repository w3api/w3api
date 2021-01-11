---
title: AbstractPreferences.getBoolean()
permalink: Java/AbstractPreferences/getBoolean
date: 2021-01-11
key: JavaJava.A.AbstractPreferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractPreferences.metodos valor="getBoolean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean getBoolean(String key, boolean def)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **boolean def**,  {% include w3api/param_description.html metodo=_dato parametro="boolean def" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractPreferences](/Java/AbstractPreferences/)

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