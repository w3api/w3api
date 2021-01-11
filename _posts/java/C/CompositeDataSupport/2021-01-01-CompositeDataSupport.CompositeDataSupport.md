---
title: CompositeDataSupport.CompositeDataSupport()
permalink: Java/CompositeDataSupport/CompositeDataSupport
date: 2021-01-11
key: JavaJava.C.CompositeDataSupport
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeDataSupport.constructores valor="CompositeDataSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompositeDataSupport(CompositeType compositeType, String[] itemNames, Object[] itemValues) throws OpenDataException
public CompositeDataSupport(CompositeType compositeType, Map<String,?> items) throws OpenDataException
~~~

## Parámetros
* **?&gt; items**,  {% include w3api/param_description.html metodo=_dato parametro="?> items" %}
* **CompositeType compositeType**,  {% include w3api/param_description.html metodo=_dato parametro="CompositeType compositeType" %}
* **Object[] itemValues**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] itemValues" %}
* **String[] itemNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] itemNames" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Excepciones
[ArrayStoreException](/Java/ArrayStoreException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [OpenDataException](/Java/OpenDataException/)

## Clase Padre
[CompositeDataSupport](/Java/CompositeDataSupport/)

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
