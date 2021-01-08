---
title: TransformerFactory.setErrorListener()
permalink: Java/TransformerFactory/setErrorListener
date: 2021-01-04
key: JavaJava.T.TransformerFactory
category: java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformerFactory.metodos valor="setErrorListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setErrorListener(ErrorListener listener)
~~~

## Parámetros
* **ErrorListener listener**,  {% include w3api/param_description.html metodo=_data parametro="ErrorListener listener" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TransformerFactory](/Java/TransformerFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransformerFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
