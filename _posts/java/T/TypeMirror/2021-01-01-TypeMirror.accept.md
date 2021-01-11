---
title: TypeMirror.accept()
permalink: Java/TypeMirror/accept
date: 2021-01-11
key: JavaJava.T.TypeMirror
category: java
tags: ['java se', 'javax.lang.model.type', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TypeMirror.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R,P> R accept(TypeVisitor<R,P> v, P p)
~~~

## Parámetros
* **P&gt; v**,  {% include w3api/param_description.html metodo=_dato parametro="P> v" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **TypeVisitor&lt;R**,  {% include w3api/param_description.html metodo=_dato parametro="TypeVisitor<R" %}

## Clase Padre
[TypeMirror](/Java/TypeMirror/)

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
