---
title: DOMResult.DOMResult()
permalink: Java/DOMResult/DOMResult
date: 2021-01-04
key: JavaJava.D.DOMResult
category: java
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
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **Node nextSibling**,  {% include w3api/param_description.html metodo=_data parametro="Node nextSibling" %}
* **Node node**,  {% include w3api/param_description.html metodo=_data parametro="Node node" %}

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
{%- for _ldc in site.data.Java.D.DOMResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
