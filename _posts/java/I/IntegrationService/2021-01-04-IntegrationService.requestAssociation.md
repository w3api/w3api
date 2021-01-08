---
title: IntegrationService.requestAssociation()
permalink: Java/IntegrationService/requestAssociation
date: 2021-01-04
key: JavaJava.I.IntegrationService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', '6.0.18']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntegrationService.metodos valor="requestAssociation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean requestAssociation(String mimetype, String[] extensions)
~~~

## Parámetros
* **String mimetype**,  {% include w3api/param_description.html metodo=_data parametro="String mimetype" %}
* **String[] extensions**,  {% include w3api/param_description.html metodo=_data parametro="String[] extensions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IntegrationService](/Java/IntegrationService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IntegrationService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
