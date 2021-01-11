---
title: AbstractPreferences.getChild()
permalink: Java/AbstractPreferences/getChild
date: 2021-01-11
key: JavaJava.A.AbstractPreferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractPreferences.metodos valor="getChild" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected AbstractPreferences getChild(String nodeName) throws BackingStoreException
~~~

## Parámetros
* **String nodeName**,  {% include w3api/param_description.html metodo=_dato parametro="String nodeName" %}

## Excepciones
[BackingStoreException](/Java/BackingStoreException/)

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
