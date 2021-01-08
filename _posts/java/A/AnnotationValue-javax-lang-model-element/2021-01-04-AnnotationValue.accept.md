---
title: AnnotationValue.accept()
permalink: Java/AnnotationValue-javax-lang-model-element/accept
date: 2021-01-04
key: JavaJava.A.AnnotationValue-javax-lang-model-element
category: java
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
* **P&gt; v**,  {% include w3api/param_description.html metodo=_data parametro="P> v" %}
* **AnnotationValueVisitor&lt;R**,  {% include w3api/param_description.html metodo=_data parametro="AnnotationValueVisitor<R" %}
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}

## Clase Padre
[AnnotationValue](/Java/AnnotationValue-javax-lang-model-element/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AnnotationValue-javax-lang-model-element.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
