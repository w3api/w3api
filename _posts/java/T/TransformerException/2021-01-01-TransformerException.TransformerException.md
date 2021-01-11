---
title: TransformerException.TransformerException()
permalink: Java/TransformerException/TransformerException
date: 2021-01-11
key: JavaJava.T.TransformerException
category: java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformerException.constructores valor="TransformerException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TransformerException(String message)
public TransformerException(String message, Throwable e)
public TransformerException(String message, SourceLocator locator)
public TransformerException(String message, SourceLocator locator, Throwable e)
public TransformerException(Throwable e)
~~~

## Parámetros
* **Throwable e**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable e" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **SourceLocator locator**,  {% include w3api/param_description.html metodo=_dato parametro="SourceLocator locator" %}

## Clase Padre
[TransformerException](/Java/TransformerException/)

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
