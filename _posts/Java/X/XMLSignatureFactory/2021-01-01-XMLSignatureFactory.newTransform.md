---
title: XMLSignatureFactory.newTransform()
permalink: /Java/XMLSignatureFactory/newTransform/
date: 2021-01-11
key: Java.X.XMLSignatureFactory
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Transform newTransform(String algorithm, TransformParameterSpec params) throws NoSuchAlgorithmException, InvalidAlgorithmParameterException
public abstract Transform newTransform(String algorithm, XMLStructure params) throws NoSuchAlgorithmException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **XMLStructure params**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStructure params" %}
* **TransformParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="TransformParameterSpec params" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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
