---
title: TabularType.TabularType()
permalink: Java/TabularType/TabularType
date: 2021-01-04
key: JavaJava.T.TabularType
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TabularType.constructores valor="TabularType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TabularType(String typeName, String description, CompositeType rowType, String[] indexNames) throws OpenDataException
~~~

## Parámetros
* **String typeName**,  {% include w3api/param_description.html metodo=_data parametro="String typeName" %}
* **String[] indexNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] indexNames" %}
* **CompositeType rowType**,  {% include w3api/param_description.html metodo=_data parametro="CompositeType rowType" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}

## Excepciones
[OpenDataException](/Java/OpenDataException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TabularType](/Java/TabularType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TabularType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
