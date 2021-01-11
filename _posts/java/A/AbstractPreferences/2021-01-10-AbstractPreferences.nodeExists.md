---
title: AbstractPreferences.nodeExists()
permalink: Java/AbstractPreferences/nodeExists
date: 2021-01-10
key: JavaJava.A.AbstractPreferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractPreferences.metodos valor="nodeExists" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean nodeExists(String path) throws BackingStoreException
~~~

## Parámetros
* **String path**,  {% include w3api/param_description.html metodo=_dato parametro="String path" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [BackingStoreException](/Java/BackingStoreException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
