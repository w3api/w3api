---
title: Preferences.exportSubtree()
permalink: Java/Preferences/exportSubtree
date: 2021-01-11
key: JavaJava.P.Preferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="exportSubtree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void exportSubtree(OutputStream os) throws IOException, BackingStoreException
~~~

## Parámetros
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}

## Excepciones
[BackingStoreException](/Java/BackingStoreException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

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
