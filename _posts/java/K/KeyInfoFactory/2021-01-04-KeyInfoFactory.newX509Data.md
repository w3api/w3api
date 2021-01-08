---
title: KeyInfoFactory.newX509Data()
permalink: Java/KeyInfoFactory/newX509Data
date: 2021-01-04
key: JavaJava.K.KeyInfoFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="newX509Data" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract X509Data newX509Data(List<?> content)
~~~

## Parámetros
* **List&lt;?&gt; content**,  {% include w3api/param_description.html metodo=_data parametro="List<?> content" %}

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
