---
title: IntegrationService.removeAssociation()
permalink: /Java/IntegrationService/removeAssociation/
date: 2021-01-11
key: Java.I.IntegrationService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', '6.0.18']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntegrationService.metodos valor="removeAssociation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean removeAssociation(String mimetype, String[] extensions)
~~~

## Parámetros
* **String[] extensions**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extensions" %}
* **String mimetype**,  {% include w3api/param_description.html metodo=_dato parametro="String mimetype" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
