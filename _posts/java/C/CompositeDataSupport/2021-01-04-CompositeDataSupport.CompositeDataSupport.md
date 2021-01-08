---
title: CompositeDataSupport.CompositeDataSupport()
permalink: Java/CompositeDataSupport/CompositeDataSupport
date: 2021-01-04
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
* **?&gt; items**,  {% include w3api/param_description.html metodo=_data parametro="?> items" %}
* **Object[] itemValues**,  {% include w3api/param_description.html metodo=_data parametro="Object[] itemValues" %}
* **String[] itemNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] itemNames" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **CompositeType compositeType**,  {% include w3api/param_description.html metodo=_data parametro="CompositeType compositeType" %}

## Excepciones
[OpenDataException](/Java/OpenDataException/), [ArrayStoreException](/Java/ArrayStoreException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CompositeDataSupport](/Java/CompositeDataSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompositeDataSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
