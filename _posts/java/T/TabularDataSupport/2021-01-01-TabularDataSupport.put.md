---
title: TabularDataSupport.put()
permalink: Java/TabularDataSupport/put
date: 2021-01-11
key: JavaJava.T.TabularDataSupport
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TabularDataSupport.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object put(Object key, Object value)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_dato parametro="Object key" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

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
