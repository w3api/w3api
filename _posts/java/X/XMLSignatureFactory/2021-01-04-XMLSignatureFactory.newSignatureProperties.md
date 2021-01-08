---
title: XMLSignatureFactory.newSignatureProperties()
permalink: Java/XMLSignatureFactory/newSignatureProperties
date: 2021-01-04
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newSignatureProperties" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SignatureProperties newSignatureProperties(List<? extends SignatureProperty> properties, String id)
~~~

## Parámetros
* **String id**,  {% include w3api/param_description.html metodo=_data parametro="String id" %}
* **List&lt;? extends SignatureProperty&gt; properties**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends SignatureProperty> properties" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[XMLSignatureFactory](/Java/XMLSignatureFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLSignatureFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
