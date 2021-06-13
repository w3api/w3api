---
title: Preferences.childrenNames()
permalink: /Java/Preferences/childrenNames/
date: 2021-01-11
key: Java.P.Preferences
category: Java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="childrenNames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String[] childrenNames() throws BackingStoreException
~~~

## Excepciones
[BackingStoreException](/Java/BackingStoreException/), [IllegalStateException](/Java/IllegalStateException/)

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
