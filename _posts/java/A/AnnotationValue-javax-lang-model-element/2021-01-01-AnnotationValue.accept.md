---
title: AnnotationValue.accept()
permalink: /Java/AnnotationValue-javax-lang-model-element/accept/
date: 2021-01-11
key: Java.A.AnnotationValue-javax-lang-model-element
category: Java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotationValue-javax-lang-model-element.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R,P> R accept(AnnotationValueVisitor<R,P> v, P p)
~~~

## Parámetros
* **AnnotationValueVisitor&lt;R**,  {% include w3api/param_description.html metodo=_dato parametro="AnnotationValueVisitor<R" %}
* **P&gt; v**,  {% include w3api/param_description.html metodo=_dato parametro="P> v" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

## Clase Padre
[AnnotationValue](/Java/AnnotationValue-javax-lang-model-element/)

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
