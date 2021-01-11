---
title: XMLSignatureFactory.newReference()
permalink: Java/XMLSignatureFactory/newReference
date: 2021-01-11
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newReference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Reference newReference(String uri, DigestMethod dm)
public abstract Reference newReference(String uri, DigestMethod dm, List<? extends Transform> transforms, String type, String id)
public abstract Reference newReference(String uri, DigestMethod dm, List<? extends Transform> transforms, String type, String id, byte[] digestValue)
public abstract Reference newReference(String uri, DigestMethod dm, List<? extends Transform> appliedTransforms, Data result, List<? extends Transform> transforms, String type, String id)
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **byte[] digestValue**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] digestValue" %}
* **List&lt;? extends Transform&gt; appliedTransforms**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Transform> appliedTransforms" %}
* **DigestMethod dm**,  {% include w3api/param_description.html metodo=_dato parametro="DigestMethod dm" %}
* **List&lt;? extends Transform&gt; transforms**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Transform> transforms" %}
* **Data result**,  {% include w3api/param_description.html metodo=_dato parametro="Data result" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XMLSignatureFactory](/Java/XMLSignatureFactory/)

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
