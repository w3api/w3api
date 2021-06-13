---
title: Transformer.transform()
permalink: /Java/Transformer/transform/
date: 2021-01-11
key: Java.T.Transformer
category: Java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transformer.metodos valor="transform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void transform(Source xmlSource, Result outputTarget) throws TransformerException
~~~

## Parámetros
* **Result outputTarget**,  {% include w3api/param_description.html metodo=_dato parametro="Result outputTarget" %}
* **Source xmlSource**,  {% include w3api/param_description.html metodo=_dato parametro="Source xmlSource" %}

## Excepciones
[TransformerException](/Java/TransformerException/)

## Clase Padre
[Transformer](/Java/Transformer/)

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
