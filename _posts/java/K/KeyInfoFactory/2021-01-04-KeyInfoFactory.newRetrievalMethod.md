---
title: KeyInfoFactory.newRetrievalMethod()
permalink: Java/KeyInfoFactory/newRetrievalMethod
date: 2021-01-04
key: JavaJava.K.KeyInfoFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="newRetrievalMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract RetrievalMethod newRetrievalMethod(String uri)
public abstract RetrievalMethod newRetrievalMethod(String uri, String type, List<? extends Transform> transforms)
~~~

## Parámetros
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **List&lt;? extends Transform&gt; transforms**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends Transform> transforms" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[KeyInfoFactory](/Java/KeyInfoFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyInfoFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
