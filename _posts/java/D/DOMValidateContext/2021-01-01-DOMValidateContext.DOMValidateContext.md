---
title: DOMValidateContext.DOMValidateContext()
permalink: /Java/DOMValidateContext/DOMValidateContext/
date: 2021-01-11
key: Java.D.DOMValidateContext
category: Java
tags: ['java se', 'javax.xml.crypto.dsig.dom', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DOMValidateContext.constructores valor="DOMValidateContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DOMValidateContext(Key validatingKey, Node node)
public DOMValidateContext(KeySelector ks, Node node)
~~~

## Parámetros
* **Node node**,  {% include w3api/param_description.html metodo=_dato parametro="Node node" %}
* **Key validatingKey**,  {% include w3api/param_description.html metodo=_dato parametro="Key validatingKey" %}
* **KeySelector ks**,  {% include w3api/param_description.html metodo=_dato parametro="KeySelector ks" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DOMValidateContext](/Java/DOMValidateContext/)

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
