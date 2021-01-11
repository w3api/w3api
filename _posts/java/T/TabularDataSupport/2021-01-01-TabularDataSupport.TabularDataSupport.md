---
title: TabularDataSupport.TabularDataSupport()
permalink: Java/TabularDataSupport/TabularDataSupport
date: 2021-01-11
key: JavaJava.T.TabularDataSupport
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TabularDataSupport.constructores valor="TabularDataSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TabularDataSupport(TabularType tabularType)
public TabularDataSupport(TabularType tabularType, int initialCapacity, float loadFactor)
~~~

## Parámetros
* **float loadFactor**,  {% include w3api/param_description.html metodo=_dato parametro="float loadFactor" %}
* **TabularType tabularType**,  {% include w3api/param_description.html metodo=_dato parametro="TabularType tabularType" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TabularDataSupport](/Java/TabularDataSupport/)

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
