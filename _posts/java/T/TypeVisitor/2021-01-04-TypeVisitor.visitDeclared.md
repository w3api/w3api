---
title: TypeVisitor.visitDeclared()
permalink: Java/TypeVisitor/visitDeclared
date: 2021-01-04
key: JavaJava.T.TypeVisitor
category: java
tags: ['java se', 'javax.lang.model.type', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TypeVisitor.metodos valor="visitDeclared" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitDeclared(DeclaredType t, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **DeclaredType t**,  {% include w3api/param_description.html metodo=_data parametro="DeclaredType t" %}

## Clase Padre
[TypeVisitor](/Java/TypeVisitor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TypeVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
