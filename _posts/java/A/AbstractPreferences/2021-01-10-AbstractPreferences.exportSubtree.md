---
title: AbstractPreferences.exportSubtree()
permalink: Java/AbstractPreferences/exportSubtree
date: 2021-01-10
key: JavaJava.A.AbstractPreferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractPreferences.metodos valor="exportSubtree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void exportSubtree(OutputStream os) throws IOException, BackingStoreException
~~~

## Parámetros
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}

## Excepciones
[IOException](/Java/IOException/), [BackingStoreException](/Java/BackingStoreException/)

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
