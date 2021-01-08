---
title: TabularData.putAll()
permalink: Java/TabularData/putAll
date: 2021-01-04
key: JavaJava.T.TabularData
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TabularData.metodos valor="putAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void putAll(CompositeData[] values)
~~~

## Parámetros
* **CompositeData[] values**,  {% include w3api/param_description.html metodo=_data parametro="CompositeData[] values" %}

## Excepciones
[KeyAlreadyExistsException](/Java/KeyAlreadyExistsException/), [NullPointerException](/Java/NullPointerException/), [InvalidOpenTypeException](/Java/InvalidOpenTypeException/)

## Clase Padre
[TabularData](/Java/TabularData/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TabularData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
