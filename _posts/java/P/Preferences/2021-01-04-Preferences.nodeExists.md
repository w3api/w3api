---
title: Preferences.nodeExists()
permalink: Java/Preferences/nodeExists
date: 2021-01-04
key: JavaJava.P.Preferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="nodeExists" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean nodeExists(String pathName) throws BackingStoreException
~~~

## Parámetros
* **String pathName**,  {% include w3api/param_description.html metodo=_data parametro="String pathName" %}

## Excepciones
[BackingStoreException](/Java/BackingStoreException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Preferences](/Java/Preferences/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Preferences.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
