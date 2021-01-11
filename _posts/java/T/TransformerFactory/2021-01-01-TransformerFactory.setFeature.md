---
title: TransformerFactory.setFeature()
permalink: Java/TransformerFactory/setFeature
date: 2021-01-11
key: JavaJava.T.TransformerFactory
category: java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformerFactory.metodos valor="setFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setFeature(String name, boolean value) throws TransformerConfigurationException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_dato parametro="boolean value" %}

## Excepciones
[TransformerConfigurationException](/Java/TransformerConfigurationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TransformerFactory](/Java/TransformerFactory/)

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
