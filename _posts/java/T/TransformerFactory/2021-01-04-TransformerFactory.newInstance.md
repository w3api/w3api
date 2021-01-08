---
title: TransformerFactory.newInstance()
permalink: Java/TransformerFactory/newInstance
date: 2021-01-04
key: JavaJava.T.TransformerFactory
category: java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformerFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static TransformerFactory newInstance() throws TransformerFactoryConfigurationError
public static TransformerFactory newInstance(String factoryClassName, ClassLoader classLoader) throws TransformerFactoryConfigurationError
~~~

## Parámetros
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader classLoader" %}
* **String factoryClassName**,  {% include w3api/param_description.html metodo=_data parametro="String factoryClassName" %}

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
