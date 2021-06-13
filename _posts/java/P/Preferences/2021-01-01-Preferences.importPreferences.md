---
title: Preferences.importPreferences()
permalink: /Java/Preferences/importPreferences/
date: 2021-01-11
key: Java.P.Preferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="importPreferences" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void importPreferences(InputStream is) throws IOException, InvalidPreferencesFormatException
~~~

## Parámetros
* **InputStream is**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream is" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [InvalidPreferencesFormatException](/Java/InvalidPreferencesFormatException/), [IOException](/Java/IOException/)

## Clase Padre
[Preferences](/Java/Preferences/)

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
