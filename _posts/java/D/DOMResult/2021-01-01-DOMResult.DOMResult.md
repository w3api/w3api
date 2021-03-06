---
title: DOMResult.DOMResult()
permalink: /Java/DOMResult/DOMResult/
date: 2021-01-11
key: Java.D.DOMResult
category: Java
tags: ['java se', 'javax.xml.transform.dom', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DOMResult.constructores valor="DOMResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DOMResult()
public DOMResult(Node node)
public DOMResult(Node node, String systemId)
public DOMResult(Node node, Node nextSibling)
public DOMResult(Node node, Node nextSibling, String systemId)
~~~

## Parámetros
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **Node node**,  {% include w3api/param_description.html metodo=_dato parametro="Node node" %}
* **Node nextSibling**,  {% include w3api/param_description.html metodo=_dato parametro="Node nextSibling" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DOMResult](/Java/DOMResult/)

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
