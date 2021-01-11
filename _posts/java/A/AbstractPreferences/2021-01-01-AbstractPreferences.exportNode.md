---
title: AbstractPreferences.exportNode()
permalink: Java/AbstractPreferences/exportNode
date: 2021-01-11
key: JavaJava.A.AbstractPreferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractPreferences.metodos valor="exportNode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void exportNode(OutputStream os) throws IOException, BackingStoreException
~~~

## Parámetros
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}

## Excepciones
[BackingStoreException](/Java/BackingStoreException/), [IOException](/Java/IOException/)

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
