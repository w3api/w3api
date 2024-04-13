---
title: Transform.transform()
permalink: /Java/Transform-javax-xml-crypto-dsig/transform/
date: 2021-01-11
key: Java.T.Transform-javax-xml-crypto-dsig
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javax-xml-crypto-dsig.metodos valor="transform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Data transform(Data data, XMLCryptoContext context) throws TransformException
Data transform(Data data, XMLCryptoContext context, OutputStream os) throws TransformException
~~~

## Parámetros
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}
* **XMLCryptoContext context**,  {% include w3api/param_description.html metodo=_dato parametro="XMLCryptoContext context" %}
* **Data data**,  {% include w3api/param_description.html metodo=_dato parametro="Data data" %}

## Excepciones
[TransformException](/Java/TransformException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Transform](/Java/Transform-javax-xml-crypto-dsig/)

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
