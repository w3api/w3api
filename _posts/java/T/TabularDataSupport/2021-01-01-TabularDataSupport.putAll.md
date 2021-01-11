---
title: TabularDataSupport.putAll()
permalink: Java/TabularDataSupport/putAll
date: 2021-01-11
key: JavaJava.T.TabularDataSupport
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TabularDataSupport.metodos valor="putAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void putAll(Map<?,?> t)
public void putAll(CompositeData[] values)
~~~

## Parámetros
* **CompositeData[] values**,  {% include w3api/param_description.html metodo=_dato parametro="CompositeData[] values" %}
* **Map&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Map<?" %}
* **?&gt; t**,  {% include w3api/param_description.html metodo=_dato parametro="?> t" %}

## Excepciones
[KeyAlreadyExistsException](/Java/KeyAlreadyExistsException/), [InvalidOpenTypeException](/Java/InvalidOpenTypeException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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
